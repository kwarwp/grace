
{'date': 'Mon Aug 01 2022 10:27:37.142 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 36
  if resposta = "A":
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 01 2022 10:27:51.339 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 47
    Tesouro().vai()
  module <module> line 44
    Texto("Vai se aventurar?", A="sim", B="não", foi=self.escolheu).vai()
  module _spy.vitollino.main line 1331
    self.cena.elt <= Popup.POP.popup
AttributeError: 'str' object has no attribute 'elt'
'''},
{'date': 'Mon Aug 01 2022 10:29:00.902 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 47
    Tesouro().vai()
  module <module> line 44
    Texto("Vai se aventurar?", A="sim", B="não", foi=self.escolheu, cena=self.templo).vai()
TypeError: __init__() got multiple values for argument 'cena'
'''},