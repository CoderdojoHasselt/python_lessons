# from io import StringIO
# import sys
#
# import builtins
#
# 
# def fake_input(prompt):
#     print(prompt)
#     return "jonny"
#
#
#
#
#
# class Capturing(list):
#     def __enter__(self):
#         self._stdout = sys.stdout
#         sys.stdout = self._stringio = StringIO()
#         self._input = builtins.input
#         builtins.input = fake_input
#         return self
#     def __exit__(self, *args):
#         self.extend(self._stringio.getvalue().splitlines())
#         del self._stringio    # free up some memory
#         sys.stdout = self._stdout
#         builtins.input = self._input
#
# def f():
#     print("jonny")
#
# with Capturing() as output:
#     f()
#     import main
#
# print("output")
# print(output)
