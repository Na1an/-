#!/usr/local/bin/python3

# Exercice 1.1
#
# À REMPLIR
#
# Vérifie que T est une permutation
#
def estPerm(T) :
  # À REMPLIR !!
  
  M = [False]*len(T)
  for i in range(len(T)):
    if(T[i] > len(T)): return False
    M[T[i]-1] = True

  for j in range(len(M)):
    if M[j] == False:
      return False
                 
  return True

# Exercice 1.2
#
# À REMPLIR   aaa
#
# Vérifie que T est une permutation
#   et renvoie le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def estPermOps(T) :
  ops = 0
  # À REMPLIR
  M = [False]*len(T)
  for i in range(len(T)):
    if(T[i] > len(T)): return False
    M[T[i]-1] = True

  for j in range(len(M)):
    if M[j] == False:
      return False
  ops = 5*len(T)
  return True, ops

# Exercice 1.3
#
# À REMPLIR
#
# Renvoie la permutation inverse de T
#
def inversePerm(T):
  res = [0] * len(T)
  # À COMPLÉTER
  if(estPerm(T)):
    for i in range(len(T)):
      res[T[i]-1] = i+1
    return res
  else:
    return None

# Exercice 1.4
#
# À REMPLIR
#
# Renvoie la permutation inverse de T
#   et le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def inversePermOps(T):
  res = [0] * len(T)
  ops = len(T)
  if(estPerm(T)):
    for i in range(len(T)):
      res[i] = T[len(T)-1-i]

    return res,ops
  else:
    return None,ops

# Exercice 1.5
#
# À REMPLIR xxxxxxx
#
# Calcule la permutation T2 o T1
#
def composePerm(T1, T2):
    res = [0]*len(T1)
    if len(T1) != len(T2):
        return None
    elif estPerm(T1) == False or estPerm(T2) == False : 
        return None
    else :
        for i in range(len(T1)):
            res[i] = T2[T1[i]-1]
    return res

# Exercice 1.6
#
# À REMPLIR
#
# Calcule la permutation T2 o T1
#   et renvoie le nombre de comparaisons et d'affectations effectuées par l'algorithme
#
def composePermOps(T1, T2):
  res = [0] * len(T1)
  ops = 0
  # À COMPLÉTER
  bol1,ops1 = estPermOps(T1)
  bol2,ops2 = estPermOPs(T2)

  if len(T1) != len(T2):
      return None
  elif bol1 == False or bol2 == False :
      return None
  else :
      for i in range(len(T1)):
          res[i] = T2[T1[i-1]]
  ops = ops1 + ops2
  return res, ops

##############################################################
# TESTS
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"

data_testFonction = {}	# dictionnaire {fonction:data}

def testFonction(fonction) :
  print('Test %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[:-1]		# tous les elts sauf le dernier
    ref = dt[-1]	# dernier elt
    res = fonction(*T)	# ie fonction(T[0], T[1], ...)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s' % res)
      print('    résultat attendu : %s' % ref)
  print('* Score : %d/%d\n' % (score, ldata))

def testFonctionOps(fonction) :
  print('Test %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[:-1]		# tous les elts sauf le dernier
    ref = dt[-1]	# dernier elt
    res = fonction(*T)	# ie fonction(T[0], T[1], ...)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s %d' % res)
      print('    résultat attendu : %s %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))


##############################################################
#
# Tests : estPerm
#

data_testFonction[estPerm] = [
  [[4,3,1], False],
  [[1,2,3,1], False],
  [[1,2,5,3], False],
  [[4,2,1,3], True]
  ]

##############################################################
#
# Tests : estPermOps
#

data_testFonction[estPermOps] = [
  [[3,2,1], (True, 15)],
  [[4,2,1,3], (True, 20)],
  [[3,2,3,4], (False, 15)],
  [[5,3,2,1,4], (True, 25)]
  ]


##############################################################
#
# Tests : inversePerm
#

data_testFonction[inversePerm] = [
  [[3,1,2,4], [2,3,1,4]],
  [[1,4,3,2], [1,4,3,2]],
  [[1,2,3,4], [1,2,3,4]],
  [[2,3,4,1], [4,1,2,3]],
  [[2,3,4,3], None],
  [[2,3,4], None]
  ]

##############################################################
#
# Tests : inversePermOps
#

data_testFonction[inversePermOps] = [
  [[3,1,2,4], ([2,3,1,4], 24)],
  [[3,2,4,5], (None, 20)],
  [[5,2,4,1,3], ([4,2,5,3,1], 30)]
  ]

##############################################################
#
# Tests : composePerm
#

data_testFonction[composePerm] = [
  [[4,3,2,1], [4,3,2,1], [1,2,3,4]],
  [[1,4,3,2], [1,4,3,2], [1,2,3,4]],
  [[1,4,3,2], [4,3,1,2], [4,2,1,3]],
  [[4,3,2,3], [4,3,2,1], None],
  [[1,4,3,2], [1,4,2,2], None],
  [[1,4,3], [4,3,1,2], None],
  [[1,3,2], [1,4,2,3], None]
  ]

##############################################################
#
# Tests : composePermOps
#

data_testFonction[composePermOps] = [
 [[4,3,2,1], [4,3,2,1], ([1,2,3,4], 49)], 
 [[4,2,1], [3,1,2], (None, 1)],
 [[3,2,1], [2,3,1], ([1,3,2], 37)],
 [[3,2,5,1,4], [4,3,5,2,1], ([5,3,1,4,2], 61)]
 ]

##############################################################

if __name__ == '__main__':
  for fonction in [ estPerm, inversePerm, composePerm] :
    testFonction(fonction)
  for fonction in [ estPermOps, inversePermOps, composePermOps ] :
    testFonctionOps(fonction)
