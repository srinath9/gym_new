package main
import "fmt"

func val(num int) {

num = 0
}
func ptr(num *int) {
*num = 0}

func main(){
num := 5
val(num)
fmt.Println(num)
ptr(&num)
fmt.Println(&num)
}
