
{'date': 'Mon Sep 26 2022 17:03:01.518 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: Cannot read properties of undefined (reading 'type')>
'''},
{'date': 'Mon Sep 26 2022 17:19:54.118 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  Manobras = [manobra for j in range(10) if manobra:= valido()] 
                                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Sep 26 2022 17:21:01.985 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 9
  Manobras = [manobra for j in range(10) if (manobra := valido())] 
                                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Oct 03 2022 16:57:13.389 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  def alto(self):                     #separa o azul do branco
  ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Oct 03 2022 16:58:19.687 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 52
  self.vagoes.
               ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Oct 03 2022 16:58:36.506 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 82
    testaTrem()
  module <module> line 69
    r = trem()
TypeError: __init__() missing 2 positional arguments: posicao,sinal
'''},
{'date': 'Mon Oct 03 2022 17:00:27.307 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 82
    testaTrem()
  module <module> line 69
    r = composicao()
  module <module> line 36
    self.vermelho = trem(sul, leste)   
NameError: name 'sul' is not defined
'''},