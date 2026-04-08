# Como rodar

Crie o arquivo `.env` na raiz do projeto e insira sua URI do mongodb:

```yaml
MONGO_URI=mongodb+srv://USUARIO:SENHA@HOST/?retryWrites=true&w=majority
```

Depois instalar as dependencias e rodar o `main.py`:

```bash
> pip install -r requirements.txt
> python3 main.py
```

