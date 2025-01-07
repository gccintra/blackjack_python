from pathlib import Path
import json

class DataRecord:
    """Banco de dados JSON para os recursos Gerente e Empregados."""

    def __init__(self, filename):
        base_path = Path(__file__).parent.parent
        self.__data_folder = base_path / "data"
        self.__data_folder.mkdir(exist_ok=True)
        self.__filename = self.__data_folder / filename

        self.__models = []
        self.read()

    def read(self):
            try:
                if not self.__filename.exists(): 
                    print(f"O arquivo {self.__filename} não existe! Criando um novo arquivo.")
                    self.__filename.touch() 
                    self.save() 
                else:
                    with open(self.__filename, "r", encoding="utf-8") as fjson:
                        self.__models = json.load(fjson)
            except json.JSONDecodeError:
                print(f"Erro ao ler o arquivo {self.__filename}. O arquivo pode estar corrompido.")
                self.__models = []
                
    def write(self, model):
        try:
            self.__models.append(model) 
            self.save()
            return True
        except Exception as e:
            print(f"Erro ao adicionar o modelo: {e}")
            return False

    def save(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as fjson:
                json.dump(self.__models, fjson, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def get_models(self):
        self.read()
        return self.__models

    def update_user(self, username, updated_data):
        for record in self.__models:
            if record["username"] == username:
                record.update(updated_data) 
                self.save()
                return True
        return False