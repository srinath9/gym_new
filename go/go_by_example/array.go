package main
import "fmt"

func main(){

var a[5] int
fmt.Println("emp : ",a)
a[4] = 100
fmt.Println(a[4])
fmt.Println(len(a))
b:=[5] int {1,2,3,6,78}
fmt.Println("dcl : ",b)

var two[2][3] int 
for  i:=0;i<2;i++{
for j:=0;j<3;j++{
two[i][j]=i+j
}}
fmt.Println("2d : ",two)

}
