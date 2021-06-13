<p align="center">
  <img width="756" alt="X111" img src="https://user-images.githubusercontent.com/76184559/121821412-c17f2d80-cc66-11eb-9865-60b91880fb60.PNG"/>
</p>

Thynnus provides a new feature, annotation, to Python checking the element is meant to override an element declared in a superclass. Thynnus is in a single file with no dependencies other than the [Python Standard Library](https://docs.python.org/3/library/).

## Case I

- Define the base class.

```python
class A:
    def m(self):
        pass
```

- Extend the base class and override method.

```python
class B(A):
    @override(A)
    def m(self):
        pass

    @override(A)
    def n(self):
        pass
```

- Method `B.m` will not cause any errors, but `B.n` will show indicating the method is not found in the parent class `A`.

```
annotation.NoSuperClassMethodFound: No method named n found in superclass.
```

## Case II (Working in Progress)

- Give the classes `A` and `B` below:

```python
class A:
    def m(self):
        pass

class B(A):
    pass
```

- Override is declared without pointing to a specific superclass.

```python
class C(B):
    @override
    def m(self):
        pass
```

- The decorator will inspect all superclasses and check if a method  `m` can be override using `inspect.getmro`.

## Case III (Working in Progress)

- The decorator will not only check a method under the same name but also compare the decorated method's signature to the superclass method's signature. For example, the case below generates an error because the signature does not match.

```python
class A:
    def m(self) -> int:
        pass

class B(A):
    @override
    def m(self) -> str:
        pass
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/SFL09/Thynnus/blob/main/LICENSE) file for details.
