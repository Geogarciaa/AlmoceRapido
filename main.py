#Programação Orientada a Objetos
#Profª: Camila Serrão
#Alunos: Geova Garcia, Theo Henrique e Ítalo Silva
#2º Informática Matutino

#----------------------------------------------------------------
import classes

#OBJ_ALUNOS-----------------------------------------------
print('\n==========Alunos==========\n')

aluno1 = classes.Aluno('Theo Henrique', 'theoh007@gamil.com', 'theo123', '996568723', 'Informática', '2 M', '123.456.789-10', '2023104050544')
aluno1.cadastrar()
aluno1.logar()

aluno2 = classes.Aluno('italo', 'italosebastian49@gmail.com', 'italo123', '993798556', 'Informática', '2 M', '066.324.092-10', '2023106060051')
aluno2.cadastrar()
aluno2.logar()

aluno3 = classes.Aluno('Geovana', 'geovana04@gmail.com', 'geo123', '992345676', 'Informática', '2 M', '078.098.065-08', '2023106060087')
aluno3.cadastrar()
aluno3.logar()

aluno4 = classes.Aluno('Alice', 'alicinha0@gmail.com', 'lice123', '9923907676', 'Informática', '2 V', '098.748.089-08', '2023106060090')
aluno4.cadastrar()
aluno4.logar()

#OBJS_RESTAURANTE-------------------------------------
print('\n==========Restaurantes==========\n')

restaurante = classes.Restaurante('RestauranteIF' , 'restauranteif@gmail', 'restauranteif123', '993798556', '563.537.999-98', '7853018', 'MarcosLanches')
restaurante.cadastrar()
restaurante.logar()

restaurante2 = classes.Restaurante('RestauranteEsquina' , 'restauranteEsquina@gmail', 'restauranteEq123', '993764536', '993.777.569-28', '7322118', 'Lulupão')
restaurante2.cadastrar()
restaurante2.logar()

restaurante3 = classes.Restaurante('RestaurantePaodeQ' , 'restaupaoqueijof@gmail', 'resqueijo123', '993763011', '730.994.998-02', '7332987', 'jujugoiaba')
restaurante3.cadastrar()
restaurante3.logar()

restaurante4 = classes.Restaurante('Fritosrestaurante' , 'Friturasif@gmail', 'frito123', '620174683', '644.955.122-90', '8839213', 'Arthurfritos')
restaurante4.cadastrar()
restaurante4.logar()

#OBJ_VISITANTE---------------------------------------------------------
print('\n==========Visitantes==========\n')

Visitante1 = classes.Visitantes('Lucas', 'Lucasrib19@gmail', 'Lulu323', '993798556', '241.642.431-12')
Visitante1.cadastrar()
Visitante1.logar()

Visitante2 = classes.Visitantes('Pedro', 'pepe10@gmail.com', 'pedro323', '992453678', '245.602.031-97')
Visitante1.cadastrar()
Visitante1.logar()

Visitante2 = classes.Visitantes('Luísa', 'Luisaa@gmail.com', 'Luisaa21', '993745365', '041.882.123-12')
Visitante1.cadastrar()
Visitante1.logar()

Visitante1 = classes.Visitantes('Julia', 'julinha@gmail', 'ju567', '40028922', '141.612.131-00')
Visitante1.cadastrar()
Visitante1.logar()

#OBJ_DEPAE-------------------------------
print('\n==========Funcionários do DEPAE==========\n')

DapaeFunc = classes.Func_Depae('Roberto', 'RobertoDepae@gmail', 'Robs564', '994567879', '177.633.901-17', '673921')
DapaeFunc.cadastrar()
DapaeFunc.logar()

DapaeFunc1 = classes.Func_Depae('Kaio', 'KaioDepae@gmail', 'Kaio64', '5569326', '987.113.881-17', '6657112')
DapaeFunc1.cadastrar()
DapaeFunc1.logar()

DapaeFunc3 = classes.Func_Depae('Lucas', 'LucasDepae@gmail', 'Lucas402', '9812325', '032.244.677-14', '5654909')
DapaeFunc3.cadastrar()
DapaeFunc3.logar()

DapaeFunc4 = classes.Func_Depae('Nicolas', 'NicolasDepae@gmail', 'Nicolas78', '3296730', '695.896.534-16', '6893343')
DapaeFunc4.cadastrar()
DapaeFunc4.logar()