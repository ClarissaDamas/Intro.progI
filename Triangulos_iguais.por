programa {
  funcao inicio() 
  {
    inteiro n1,n2,n3,n4 
    escreva("digite tres valores\n")
    leia(n1,n2,n3)

    se(n1 == n2 == n3)
    {
      escreva("este e um triangulo equilatero")
    }
    senao se(n1==n2 ou n2==n3 ou n1==n3)
    {
      escreva("triangulo isosceles")
    }
    senao
    {
    escreva("triangulo escaleno|")
    }
    escreva("\n")
  }
}
