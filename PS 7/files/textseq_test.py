
from random import choice
from word2vec import word2vec, exampleCorpus
import numpy as np
import re
from collections import deque
'''
TODO: 
Implement training
Opt: Implement context vector handler?
Opt: Implement attention?
'''
class textSeq2Seq:
    def __init__(self, inputdims=4, limit=100):
        self.vs = inputdims
        self.limit = limit
        
        
        self.cell_enc = np.zeros(inputdims)
        self.hidden_enc = np.zeros(inputdims)
        
        self.forgetW_enc = np.random.randn(inputdims*2, inputdims)
        self.forgetB_enc = np.zeros(inputdims)
        
        self.inputmagW_enc = np.random.randn(inputdims*2, inputdims)
        self.inputmagB_enc = np.zeros(inputdims)
        self.inputdataW_enc = np.random.randn(inputdims*2, inputdims)
        self.inputdataB_enc = np.zeros(inputdims)
        
        self.outputcellW_enc = np.random.randn(inputdims, inputdims)
        self.outputcellB_enc = np.zeros(inputdims)
        self.outputinW_enc = np.random.randn(inputdims*2, inputdims)
        self.outputinB_enc = np.zeros(inputdims)
        
        
        self.cell_dec = np.zeros(inputdims)
        self.hidden_dec = np.zeros(inputdims)
        
        self.forgetW_dec = np.random.randn(inputdims*2, inputdims)
        self.forgetB_dec = np.zeros(inputdims)
        
        self.inputmagW_dec = np.random.randn(inputdims*2, inputdims)
        self.inputmagB_dec = np.zeros(inputdims)
        self.inputdataW_dec = np.random.randn(inputdims*2, inputdims)
        self.inputdataB_dec = np.zeros(inputdims)
        
        self.outputcellW_dec = np.random.randn(inputdims, inputdims)
        self.outputcellB_dec = np.zeros(inputdims)
        self.outputinW_dec = np.random.randn(inputdims*2, inputdims)
        self.outputinB_dec = np.zeros(inputdims)
    
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def d_sigmoid(self, x):
        return self.sigmoid(x) * (1-self.sigmoid(x))
    
    def tanh(self, x):
        return np.tanh(x)

    def d_tanh(self, x):
        return 1 - (self.tanh(x)**2)
    
    

    def ff_sig_layer(self, i, W, B=0):
        z = np.dot(i, W) + B
        return z, self.sigmoid(z)

    def ff_tanh_layer(self, i, W, B=0):
        z = np.dot(i, W) + B
        return z, self.tanh(z)

    
    def LSTM_step(self, 
            cell, hidden, input, 
            forgetW, forgetB, 
            inputmagW, inputmagB, 
            inputdataW, inputdataB,
            outputcellW, outputcellB, 
            outputinW, outputinB
        ):
        hidNin = np.concatenate((hidden, input), axis = None)
        
        cellforget_z, cellforget_a = self.ff_sig_layer(hidNin, forgetW, forgetB)
        cell = np.multiply(cell, cellforget_a)
        
        inputmag_z, inputmag_a = self.ff_sig_layer(hidNin, inputmagW, inputmagB)
        inputdata_z, inputdata_a = self.ff_tanh_layer(hidNin, inputdataW, inputdataB)
        cell = np.add(cell, np.multiply(inputmag_a, inputdata_a))
        
        outputcell_z, outputcell_a = self.ff_tanh_layer(cell, outputcellW, outputcellB)
        outputin_z, outputin_a = self.ff_sig_layer(hidNin, outputinW, outputinB)
        output = np.multiply(outputcell_a, outputin_a)
        hidden = output
        
        return cell, hidden, output, hidNin, cellforget_a, cellforget_z, inputmag_z, inputmag_a, inputdata_z, inputdata_a, outputcell_z, outputcell_a, outputin_z, outputin_a

    
    def encoder_LSTM(self, x): 
        propopack = deque()
        for item in x:
            self.cell_enc, self.hidden_enc, output, hidNin, cellforget_a, cellforget_z, inputmag_z, inputmag_a, inputdata_z, inputdata_a, outputcell_z, outputcell_a, outputin_z, outputin_a = self.LSTM_step(
                self.cell_enc, self.hidden_enc, item,
                self.forgetW_enc, self.forgetB_enc,
                self.inputmagW_enc, self.inputmagB_enc,
                self.inputdataW_enc, self.inputdataB_enc,
                self.outputcellW_enc, self.outputcellB_enc,
                self.outputinW_enc, self.outputinB_enc
            )
            propopack.appendleft((self.cell_enc, self.hidden_enc, output, hidNin, cellforget_a, cellforget_z, inputmag_z, inputmag_a, inputdata_z, inputdata_a, outputcell_z, outputcell_a, outputin_z, outputin_a))
        return self.hidden_enc, propopack
        
    def decoder_LSTM(self, cv, training):
        out = list()
        propopack = deque()
        for i in range(self.limit):
            self.cell_dec, self.hidden_dec, output, hidNin, cellforget_a, cellforget_z, inputmag_z, inputmag_a, inputdata_z, inputdata_a, outputcell_z, outputcell_a, outputin_z, outputin_a = self.LSTM_step( 
                self.cell_dec, self.hidden_dec, cv,
                self.forgetW_dec, self.forgetB_dec,
                self.inputmagW_dec, self.inputmagB_dec,
                self.inputdataW_dec, self.inputdataB_dec,
                self.outputcellW_dec, self.outputcellB_dec,
                self.outputinW_dec, self.outputinB_dec
            )
            propopack.appendleft((self.cell_dec, self.hidden_dec, output, hidNin, cellforget_a, cellforget_z, inputmag_z, inputmag_a, inputdata_z, inputdata_a, outputcell_z, outputcell_a, outputin_z, outputin_a))
            out.append(output)          
            if output is not cv and self.Tw2v.getMostSimilar(output) == 'eos' and training:
                break
        out = np.array(out)
        return out, propopack
    
    
    def forward(self, x, training=False):
        cv, propopack_enc = self.encoder_LSTM(x)
        outseq, propopack_dec = self.decoder_LSTM(cv, self.limit, training)
        return outseq, propopack_enc, propopack_dec
    
    def predict(self, sntc):
        
        sntc += ' eos'
        try:
            vectors = self.Xw2v.getVec(re.split(r'\s+', str(sntc)))
        except NameError:
            print('ERROR: MODEL NOT TRAINED!')
        
        e, nonsense1, nonsense2 = self.forward(vectors[:-1:-1] + vectors[-1], self.limit)
        outvectors = e[:-1] if self.Tw2v.getMostSimilar(e[-1]) == 'eos' else e
        
        outsentc = str()
        for vector in outvectors:
            outsentc += self.Tw2v.getMostSimilar(vector) + ' '
        return outsentc
    
    
    def trainStep(self, inputs, learning_rate=0.01):
        xseq = inputs[0][:-1:-1] + inputs[0][-1]
        tseq = inputs[1]

        yseq, propopack_enc, propopack_dec = self.forward(xseq, True)
        
        
        
        if len(tseq) < self.limit:
            while len(tseq) < self.limit:
                tseq = np.append(tseq, self.Tw2v.getVec('eos'))
        elif len(tseq) > self.limit:
            raise ValueError(f'Training data sample too large (above {self.limit} tokens)')
        tseq = tseq[::-1]

        
        
        
        
        ''' LSTM CODE:
        hidNin = np.concatenate((hidden, input), axis = None)
        
        cellforget_z, cellforget_a = self.ff_sig_layer(hidNin, forgetW, forgetB)
        cell = np.multiply(cell, cellforget_a)
        
        inputmag_z, inputmag_a = self.ff_sig_layer(hidNin, inputmagW, inputmagB)
        inputdata_z, inputdata_a = self.ff_tanh_layer(hidNin, inputdataW, inputdataB)
        cell = np.add(cell, np.multiply(inputmag_a, inputdata_a))
        
        outputcell_z, outputcell_a = self.ff_tanh_layer(cell, outputcellW, outputcellB)
        outputin_z, outputin_a = self.ff_sig_layer(hidNin, outputinW, outputinB)
        output = np.multiply(outputcell_a, outputin_a)
        hidden = output

        Product rule = Df(x)g(x)/Dx = f(x) * Dg(x)/Dx + g(x) * Df(x)/Dx
        Df(x,y)/Dx = y
        Df(x,y)/Dy = x
        '''
        
        
        
        d_dec_outputin = np.zeros(self.vs)
        d_dec_outputcell = np.zeros(self.vs)
        d_dec_inputmag = np.zeros(self.vs)
        d_dec_inputdata = np.zeros(self.vs)
        d_dec_cellforget = np.zeros(self.vs)

        d_dec_hidNin = np.zeros(self.vs*2)
        d_output = np.zeros(self.vs)
        for i, propo_step in enumerate(propopack_dec):
            np.add(d_output, np.subtract(tseq[i], propo_step[2]))
            
            d_dec_outputin_current = d_output * propo_step[11] * self.d_sigmoid(propo_step[12])
            np.add(d_dec_outputin, np.multiply(d_dec_outputin_current, propo_step[3]))
            np.add(d_dec_hidNin, np.dot(d_dec_outputin_current, self.outputinW_dec))
            d_dec_outputcell_current = d_output * propo_step[13] * self.d_sigmoid(propo_step[10])
            np.add(d_dec_outputcell, np.multiply(d_dec_outputcell_current, propo_step[0]))
            
            d_dec_cell_input_completed = np.dot(d_dec_outputcell_current, self.outputcellW_dec)
            d_dec_inputmag_current = d_dec_cell_input_completed * propo_step[9] * self.d_sigmoid(propo_step[6])
            np.add(d_dec_inputmag, np.multiply(d_dec_inputmag_current, propo_step[3]))
            np.add(d_dec_hidNin, np.dot(d_dec_inputmag_current, self.inputmagW_dec))
            d_dec_inputdata_current = d_dec_cell_input_completed * propo_step[7] * self.d_tanh(propo_step[8])
            np.add(d_dec_inputdata, np.multiply(d_dec_inputdata_current, self.inputmagW_dec))
            np.add(d_dec_hidNin, np.dot(d_dec_inputdata_current, self.inputdataW_dec))
            
            oldcell = np.subtract(propo_step[0], np.multiply(propo_step[7], propo_step[9]))
            d_dec_cellforget_current = d_dec_cell_input_completed * oldcell * self.d_sigmoid(propo_step[5])
            np.add(d_dec_cellforget, np.multiply(d_dec_cellforget_current, propo_step[3]))
            np.add(d_dec_hidNin, np.dot(d_dec_cellforget_current, self.forgetW_dec))
            
            d_output = np.zeros(self.vs)
            np.add(d_output, d_dec_hidNin[:self.vs//2])

        
        
        d_output = d_dec_hidNin[self.vs//2:]
        for i, propo_step in enumerate(propopack_enc):
            np.add(d_output, np.subtract(tseq[i], propo_step[2]))
            
            d_dec_outputin_current = d_output * propo_step[11] * self.d_sigmoid(propo_step[12])
            np.add(d_dec_outputin, d_dec_outputin_current)
            np.add(d_hidNin, np.dot(d_dec_outputin_current, self.outputinW_dec))
            d_dec_outputcell_current = d_output * propo_step[13] * self.d_sigmoid(propo_step[10])
            np.add(d_dec_outputcell, d_dec_outputcell_current)
            
            d_dec_cell_input_completed = np.dot(d_dec_outputcell_current, self.outputcellW_dec)
            d_dec_inputmag_current = d_dec_cell_input_completed * propo_step[9] * self.d_sigmoid(propo_step[6])
            np.add(d_dec_inputmag, d_dec_inputmag_current)
            np.add(d_hidNin, np.dot(d_dec_inputmag_current, self.inputmagW_dec))
            d_dec_inputdata_current = d_dec_cell_input_completed * propo_step[7] * self.d_tanh(propo_step[8])
            np.add(d_dec_inputdata, d_dec_inputdata_current)
            np.add(d_hidNin, np.dot(d_dec_inputdata_current, self.inputdataW_dec))
            
            oldcell = np.subtract(propo_step[0], np.multiply(propo_step[7], propo_step[9]))
            d_dec_cellforget_current = d_dec_cell_input_completed * oldcell * self.d_sigmoid(propo_step[5])
            np.add(d_dec_cellforget, d_dec_cellforget_current)
            np.add(d_hidNin, np.dot(d_dec_cellforget_current, self.forgetW_dec))
            
            d_output = np.zeros(self.vs)
            np.add(d_hidNin[:self.vs//2])

        

        

        
    def trainAll(self, Xcorpus=exampleCorpus, Tcorpus=exampleCorpus, areFiles=False, num_epochs=750, learning_rate=0.01):
        if not areFiles:
            Xcorpus = [sentence + ' eos' for sentence in Xcorpus]
            Tcorpus = [sentence + ' eos' for sentence in Tcorpus]
        else:
            with open(Xcorpus, 'r') as Xf:
                with open(Tcorpus, 'r') as Tf:
                    Xcorpus = [sentence + ' eos' for sentence in Xf.readlines()]
                    Tcorpus = [sentence + ' eos' for sentence in Tf.readlines()]
        self.Xw2v = word2vec(Xcorpus, self.vs)
        self.Tw2v = word2vec(Tcorpus, self.vs)

        sentence_vectors_x = [self.Xw2v.getVec(re.split(r'\s+', str(sentence))) for sentence in Xcorpus]
        sentence_vectors_t = [self.Tw2v.getVec(re.split(r'\s+', str(sentence))) for sentence in Tcorpus]

        pool = list()
        for i in range(len(sentence_vectors_x)):
            pool.append((sentence_vectors_x[i], sentence_vectors_t[i]))
        for epoch in range(num_epochs):
            for i in range(10):
                self.trainStep(choice(pool), learning_rate)

if __name__ == '__main__': 
    model = textSeq2Seq()
    model.trainAll()

    
    print(model.predict('The dog runs in the park'))
    print(model.predict('She loves to read a book'))
    print(model.predict('He ate a sandwich with his friends'))
