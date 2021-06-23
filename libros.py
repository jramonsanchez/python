def libros():
    import collections
    libros = ["La caída de los gigantes", "El apostador", "El apostador", "El psicoanalista", "El psicoanalista", "Viaje al fin de la noche", "La caída de los gigantes", "Puente a la realidad", "La caída de los gigantes", "El psicoanalista"]
    print(collections.Counter(libros))


def libros2():
    import collections
    libros = [];
    while True:
        entrada = input('Escribe un libro: ')
        libros.append(entrada)
        if not entrada: break
    libros.pop()
    print(collections.Counter(libros))
