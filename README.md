# M5 - Kopa do Mundo

## Preparando ambiente para execução dos testes
### Procedimentos para rodar os testes da tarefa 1
1. Faça a instalação das bibliotecas de teste:
```shell
pip install pytest-testdox pytest-django
```
2. Use o comando abaixo para rodar os testes referentes à tarefa 1:
```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```
---
### Procedimentos para rodar os testes a partir da tarefa 2
1. Verifique se os pacotes pytest, pytest-testdox e/ou pytest-django estão instalados globalmente em seu sistema:
```shell
pip list
```
2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```
3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```


5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```

6. Como, a partir da tarefa 2, você utilizará Django, é necessário criar um arquivo bem importante: **pytest.ini**. Crie-o na raiz do projeto e adicione dentro dele o seguindo texto:
```python
[pytest]
DJANGO_SETTINGS_MODULE = kopa_do_mundo.settings
```

Após isso, você pode executar os comandos abaixo para rodar os testes (inclusive da tarefa 1):
- Tarefa 1

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Tarefa 2

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```

- Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

- Tarefa 4

```shell
pytest --testdox -vvs tests/tarefas/tarefa_4/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo: executar somente "test_object_representation"

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_model.py::TeamModelTest::test_object_representation
```

Caso queira, também é possível rodar todos os testes de uma vez:
```shell
pytest --testdox -vvs
```
