# TP-pyqt1

https://thomaspietrzak.com/teaching/IHM/TP-pyqt1.html

### Question 1: Que faut il ne pas oublier pour que le code s'execute? Que voyez vous au print?
il faut rajouter : 
```python
sys.exit(app.exec_())
```
On peut voir les arguments passé + le nom du fichier.

### Question 2.1: une erreur se produit à l'execution ? Que devez vous faire pour la corriger ?
il ne faut pas oublier d'init QMainWindow : 
```python
QMainWindow.__init__(self)
```

### Question 2.2: Pourquoi la fenêtre ne s'affiche pas? que faut il rajouter?

### Question 4: Comment connecter les actions aux slots ?

Grâce à 
```python
copyFile.triggered.connect(self.copy_file)
```

### Question 6: Le code ne s'execute pas correctement car vous n'avez pas acces au textEdit depuis la méthode open ou save. Comment résoudre ce problème?

il faut mettre le text edit en globale : 
```python
self.textEdit = QTextEdit()
self.setCentralWidget(self.textEdit)
```



