package main

import (
    "fmt"
    "time"
)

func pinger(c chan string) {
    for i := 0; ; i++ {
        c <- "ping"
	fmt.Println("doing")
    }
}
func printer(c chan string) {
    for {
        msg := <- c
        fmt.Println(msg)
	fmt.Println("printer")
        time.Sleep(time.Second * 1)
    }
}
func main() {
    var c chan string = make(chan string)
    
    go pinger(c)
    go printer(c)
    
    var input string
    fmt.Scanln(&input)
}
