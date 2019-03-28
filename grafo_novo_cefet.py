
class Vertice:

    def __init__(self, nome):
        self.nome = nome
        self.listaAdj =[]
        self.visitado ='branco'
        self.anterior =''
class Grafo:

    def __init__(self):
        self.fila = []
        self.pilha = []
        self.verticeLista = []
        self.armazenaOrdem = []
        self.count=0

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
    
    def buscaEmProfundidadePreOrdem(self,verticeInicial:Vertice):
        print ("Olhei o %s vertice"%verticeInicial.nome)
        verticeInicial.visitado="cinza"
        self.pilha.append(verticeInicial)

        while(self.pilha!=[]):
            v = self.pilha.pop()
            self.armazenaOrdem.append(v)
            v.visitado = "preto"
            self.count-=1
            print ("Visitei o %s vertice"%v.nome)            
            for a in v.listaAdj:
                if(a.visitado!='preto'):
                    print('Empilhei para percorrer %s'%a.nome)
                    self.buscaEmProfundidadePreOrdem(a)
    
    def buscaEmProfundidadePosOrdem(self,verticeInicial:Vertice):#errado tá faltando o momento em que desempilha o último
        

        while(verticeInicial.visitado!='cinza'):
            print ("Percorrer %s vertice"%verticeInicial.nome)
            verticeInicial.visitado="cinza"
            self.pilha.append(verticeInicial)
               
            for a in verticeInicial.listaAdj:
                if(a.visitado!='cinza'):
                    print('Empilhei para percorrer %s'%a.nome)
                    self.buscaEmProfundidadePosOrdem(a)
                    self.armazenaOrdem.append(self.pilha.pop())
                                                    
    
    def printArmazenaOrdem(self):
        for o in self.armazenaOrdem:
            print(o.nome)

    def temCaminho(self,vertice:Vertice):
        retorna = None
        for v in vertice:
            if (v.visitado!="cinza"):
                retorna=v
        
        return retorna
    

if __name__=="__main__":

    grafo = Grafo()
    grafo.carregaListaVerticeCarga('carga.txt')
    #grafo.buscaEmLargura(grafo.verticeLista[5])
    #grafo.buscaEmProfundidadePreOrdem(grafo.verticeLista[0])
    grafo.buscaEmProfundidadePosOrdem(grafo.verticeLista[0])
    grafo.printArmazenaOrdem()