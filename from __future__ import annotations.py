from abc import ABC, abstractmethod

# Interface para representar um documento
class Documento(ABC):
    @abstractmethod
    def abrir(self) -> str:
        pass

# Subclasses concretas de Documento (produtos concretos)
class DocumentoPDF(Documento):
    def abrir(self) -> str:
        return "Abrindo documento PDF..."

class DocumentoWord(Documento):
    def abrir(self) -> str:
        return "Abrindo documento do Word..."

class DocumentoTexto(Documento):
    def abrir(self) -> str:
        return "Abrindo documento de texto..."

# Interface para criadores de documentos (criador abstrato)
class FabricaDeDocumentos(ABC):
    @abstractmethod
    def criar_documento(self) -> Documento:
        pass

# Subclasses concretas de FabricaDeDocumentos (criadores concretos)
class FabricaPDF(FabricaDeDocumentos):
    def criar_documento(self) -> Documento:
        return DocumentoPDF()

class FabricaWord(FabricaDeDocumentos):
    def criar_documento(self) -> Documento:
        return DocumentoWord()

class FabricaTexto(FabricaDeDocumentos):
    def criar_documento(self) -> Documento:
        return DocumentoTexto()

# Função cliente para criar e abrir documentos
def cliente_criar_e_abrir_documento(criador: FabricaDeDocumentos) -> None:
    documento = criador.criar_documento()
    print(f"Cliente: Criou e agora está abrindo um documento.\n{documento.abrir()}\n")

if __name__ == "__main__":
    print("Cliente: Usando uma fábrica de documentos PDF.")
    cliente_criar_e_abrir_documento(FabricaPDF())

    print("Cliente: Usando uma fábrica de documentos do Word.")
    cliente_criar_e_abrir_documento(FabricaWord())

    print("Cliente: Usando uma fábrica de documentos de texto.")
    cliente_criar_e_abrir_documento(FabricaTexto())