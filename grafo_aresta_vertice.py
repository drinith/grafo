
class Vertice:

    def __init__(self, nome):
        self.nome = nome
        self.listaAdj =[]
        self.visitado ='branco'
        self.time=0
        self.anterior=None
        self.distancia=0

class Aresta:

    def __init__(self, vertice1,vertice2,peso):
        self.v1 = vertice1
        self.v2 = vertice2
        self.peso = peso
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
                                a = Aresta(v,v2,int(aresta[2]))
                                v.listaAdj.append(a)

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
                    if w.v2.visitado!='preto':
                        print('Olhei '+w.nome+' ficou cinza') 
                        w.v2.visitado ="cinza"
                        self.fila.append(w.v2)
                        print (w.v2.nome)
    
    def buscaEmProfundidadePreOrdem(self,vertice:Vertice):
        self.time = self.time+1
        vertice.time= self.time
        print ("vertice %s distancia = %d"% (vertice.nome,vertice.time))
        vertice.visitado='cinza'
        print('vistita %s'%(vertice.nome))
        self.armazenaOrdem.append(vertice)
        for arestaAdj in vertice.listaAdj:
            vertice.anterior = arestaAdj.v2
            if arestaAdj.v2.visitado =="branco": 
                self.buscaEmProfundidadePreOrdem(arestaAdj.v2)
        vertice.visitado='preto'
        print('Acaba %s'%(vertice.nome))
        
    def caminhoDijkstra(self,vertice:Vertice):
        vertice.visitado="preto"
        for aresta in vertice.listaAdj:
            aresta.v2.visitado="cinza"
            # distancia de vertice inicial mais aresta peso é menor que peso do vertice 2 
            if (aresta.v2.distancia>vertice.distancia+aresta.peso):
                aresta.v2.anterior = vertice
                aresta.v2.distancia = vertice.distancia+aresta.peso
        #Buscar vertice com menor distancia
        distancia =99999999999999999
        verticeMenor =" "
        for a in vertice.listaAdj:
             if (a.v2.distancia<distancia):
                distancia=a.v2.distancia
                verticeMenor = a.v2
        if verticeMenor!=" ":
            print ("Para a raiz o vertice %s tem peso %d vindo por %s" % (verticeMenor.nome,verticeMenor.distancia,verticeMenor.anterior.nome))       
            self.caminhoDijkstra(verticeMenor)

    def inicializacaoDijkstra(self,vRaiz:Vertice):
        for vertice in self.verticeLista:
            if(vRaiz.nome==vertice.nome):
                vRaiz.anterior=None
                vRaiz.distancia=0
            else:
                vertice.anterior =None
                vertice.distancia=999999999999999 

        return vRaiz
        
    def buscaEmProfundidadePosOrdem(self,vertice:Vertice):
        self.time = self.time+1
        vertice.time= self.time
        print ("vertice %s distancia = %d"% (vertice.nome,vertice.time))
        vertice.visitado='cinza'
        print('vistita %s'%(vertice.nome))
        for arestaAdj in vertice.listaAdj:
            vertice.anterior = arestaAdj.v2
            if arestaAdj.v2.visitado =="branco": 
                self.buscaEmProfundidadePreOrdem(arestaAdj.v2)
        vertice.visitado='preto'
        print('Acaba %s'%(vertice.nome))
        self.armazenaOrdem.append(vertice)
  
    def imprimirVerticesCaminhos(self):

        for v in self.verticeLista:
            if v.anterior is not None:
                print ('Vertice %s tem caminho de %s com peso %d' %(v.nome,v.anterior.nome ,v.distancia))
            else:
                print ('Vertice %s tem caminho de %s com peso %d' %(v.nome,"raiz",v.distancia))


    def printArmazenaOrdem(self):
       
        sequencia=" "
        for o in self.armazenaOrdem:
            sequencia = sequencia+"->"+o.nome
        print(sequencia)   



if __name__=="__main__":

    grafo = Grafo()
    grafo.carregaListaVerticeCarga('carga_aresta.txt')
    #grafo.buscaEmLargura(grafo.verticeLista[5])
    # grafo.buscaEmProfundidadePreOrdem(grafo.verticeLista[0])
    # grafo.printArmazenaOrdem()
    # grafo.armazenaOrdem=[]
    # grafo.buscaEmProfundidadePosOrdem(grafo.verticeLista[0])
    # grafo.printArmazenaOrdem()

    #Passando o valor saido da inicialização do dijkstra
    grafo.caminhoDijkstra(grafo.inicializacaoDijkstra(grafo.verticeLista[0]))
    grafo.imprimirVerticesCaminhos()
 

