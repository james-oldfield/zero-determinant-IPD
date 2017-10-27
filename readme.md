# zero-determinant iterated prisoner's dilemma

A simple python program to compute long-term expected payoffs of memory-1 strategies in the stochastic iterated prisoner's dilemma via Markov chain analysis.


## install

```bash
pip install requirements.txt
```

## run

#### compute long term payoffs for given probabilistic strategies

```bash
# vanilla TFT
python compute_payoffs.py --X='tft' --Y='tft'
# [3. 3.], (Given default values for outcomes)

# 3-factor extortion VS vanilla tit-for-tat
python compute_payoffs.py --X='ex-3' --Y='tft'
# [ 3.72727273  1.90909091]
```

etc.

#### general use

```bash
usage: compute_payoffs.py [-h] [--debug DEBUG] [--X X] [--Y Y] [--P_X P_X]
                          [--P_Y P_Y]

optional arguments:
  -h, --help     show this help message and exit
  --debug DEBUG  Print debug information
  --X X          Specify a named strategy for player X. See
                 `default_settings.py for more info`
  --Y Y          Specify a named strategy for player Y. See
                 `default_settings.py for more info`
  --P_X P_X      Specify the probability in vector form, for X cooperating,
                 given last round's outcomes were (CC, CD, DC, DD), e.g.
                 P_X='(1,0,1,0)'
  --P_Y P_Y      Specify a probability in vector form, for Y cooperating,
                 given last round's outcomes were (CC, DC, CD, DD), e.g.
                 P_Y='(1,1,0,0)'
```
