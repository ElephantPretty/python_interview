def my_interface(name,age,score):
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float

my_interface("alex",22,89.0)