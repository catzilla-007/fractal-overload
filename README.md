# Fractal Overload

[Fractals](https://fractalfoundation.org/resources/what-are-fractals/) are a fascinating thing that is normally
found in nature. It is a complex pattern where it makes a repetitive design. Look for a snowflake for example,
that can be considered a fractal.

With a specific bit of knowledge in programming and geometry such as recursion and linear transformation, you can also
produce interesting fractal patterns that might make you wonder how much can your computer handle the processing of the
recursion as the repetitive pattern goes smaller and smaller.


Using python opencv library and numpy, you can generate fractal patterns. Below are sample output with the level of
recursion applied.

### Usage

using pipenv

```bash
$ pipenv install
$ pipenv run fractal
```

using bare python

```bash
$ pip install numpy
$ pip install opencv-python
$ python main.py
```

code sample
```python
from image import Image
from peano import Peano

width, height = 600, 600
black = (0, 0, 0)
white = (255, 255, 255)

image = Image(height, width, black, white)
peano = Peano(image)
peano.draw(6)

# if you want to save the image
image.save_image('fractal.png')
```

### Samples

#### Koch

Level 0

![koch-level-0](img/koch-0.png)

Level 1

![koch-level-1](img/koch-1.png)

Level 2

![koch-level-2](img/koch-2.png)

Level 3

![koch-level-3](img/koch-3.png)

Level 4

![koch-level-4](img/koch-4.png)


#### Hat

Level 0

![hat-level-0](img/hat-0.png)

Level 1

![hat-level-1](img/hat-1.png)

Level 2

![hat-level-2](img/hat-2.png)

Level 3

![hat-level-3](img/hat-3.png)

Level 4

![hat-level-4](img/hat-4.png)

#### Peano

Level 0

![peano-level-0](img/peano-0.png)

Level 1

![peano-level-1](img/peano-1.png)

Level 2

![peano-level-2](img/peano-2.png)

Level 3

![peano-level-3](img/peano-3.png)

Level 4

![peano-level-4](img/peano-4.png)

### Inversed Koch

Level 0

![inv-koch-level-0](img/invkoch-0.png)

Level 1

![inv-koch-level-1](img/invkoch-1.png)

Level 2

![inv-koch-level-2](img/invkoch-2.png)

Level 3

![inv-koch-level-3](img/invkoch-3.png)

Level 4

![inv-koch-level-4](img/invkoch-4.png)
