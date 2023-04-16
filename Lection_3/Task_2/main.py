def draw_Rhombus(size, iterator=1):
    if iterator <= size:
        print(" "*(size-iterator) + "* "*iterator)
        draw_Rhombus(size, iterator+1)
    elif iterator <= 2*size:
        print(" "*(iterator-size) + "* "*(2*size - iterator))
        draw_Rhombus(size, iterator+1)
draw_Rhombus(8)



