
class Vertice:

    def __init__(self, nome):
        self.nome = nome
        self.listaAdj =[]
        self.visitado ='branco'
        self.time=0
        self.anterior=None

class Grafo:

    def __init__(self):
        self.fila = []
        self.pilha = []
        self.verticeLista = []
        self.armazenaOrdem = []
        self.time=0

    def carregaListaVerticeCarga(self,path):
        arq = open(path, 'r')
        texto = arq.readlines()
        leVertice = False
        leLigacao = False
        aresta =[]
        
        for linha in texto :
            if leVertice:
                self.verticeLista.append(Vertice(linha.replace('\n','')))#Preencgendo a lista de vertices
            if leLigacao:
                #posicao 0 da aresta é o nome do vertice
                aresta = linha.replace('\n','').split(" ")
                for v in self.verticeLista:
                    if(aresta[0]==v.nome):
                        for v2 in self.verticeLista:
                             if(aresta[1]==v2.nome):
                                 v.listaAdj.append(v2)

            if(linha=='Vertices\n'):
                leVertice=True
                leLigacao = False
            if(linha=='Ligacoes\n'):
                leVertice=False
                leLigacao = True
            #For para preencher os vertices
            
        self.count=len(self.verticeLista)       
        arq.close()

    def buscaEmLargura (self,verticeInicial:Vertice):
        verticeInicial.visitado = 'cinza'
        self.fila.append(verticeInicial)
        
        while self.fila !=[] :
                v = self.fila.pop(0)
                if(v.visitado!='preto'): 
                    v.visitado='preto'
                    print('Visitei '+v.nome+' ficou preto') 

                for w in v.listaAdj:
                    if w.visitado!='preto':
                        print('Olhei '+w.nome+' ficou cinza') 
                        w.visitado ="cinza"
                        self.fila.append(w)
                        print (w.nome)
    
    def buscaEmProfundidadePreOrdem(self,vertice:Vertice):
        self.time = self.time+1
        vertice.time= self.time
        print ("vertice %s distancia = %d"% (vertice.nome,vertice.time))
        vertice.visitado='cinza'
        print('vistita %s'%(vertice.nome))
        self.armazenaOrdem.append(vertice)
        for verticeAdj in vertice.listaAdj:
            vertice.anterior = verticeAdj
            if verticeAdj.visitado =="branco": 
                self.buscaEmProfundidadePreOrdem(verticeAdj)
        vertice.visitado='preto'
        print('Acaba %s'%(vertice.nome))
        
                
        
    def buscaEmProfundidadePosOrdem(self,vertice:Vertice):
        self.time = self.time+1
        vertice.time= self.time
        print ("vertice %s distancia = %d"% (vertice.nome,vertice.time))
        vertice.visitado='cinza'
        print('vistita %s'%(vertice.nome))
        for verticeAdj in vertice.listaAdj:
            vertice.anterior = verticeAdj
            if verticeAdj.visitado =="branco": 
                self.buscaEmProfundidadePosOrdem(verticeAdj)
        vertice.visitado='preto'
        print('Acaba %s'%(vertice.nome))
        self.armazenaOrdem.append(vertice)
  


    def printArmazenaOrdem(self):
       
        sequencia=" "
        for o in self.armazenaOrdem:
            sequencia = sequencia+"->"+o.nome
        print(sequencia)   

if __name__=="__main__":

    grafo = Grafo()
    grafo.carregaListaVerticeCarga('carga.txt')
    #grafo.buscaEmLargura(grafo.verticeLista[5])
    grafo.buscaEmProfundidadePreOrdem(grafo.verticeLista[0])
    grafo.printArmazenaOrdem()
    # grafo.armazenaOrdem=[]
    # grafo.buscaEmProfundidadePosOrdem(grafo.verticeLista[0])
    # grafo.printArmazenaOrdem()
    
 

