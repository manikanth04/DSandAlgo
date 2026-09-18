package main

import (
	"fmt"
	"math/rand"
	"time"
)

func countZeros(c []int) int {
	l := 0
	r := len(c) - 1

	for r-l > 1 {

		m := (l + (r-l)/2)

		if c[m] == 0 {
			l = m
		} else {
			r = m - 1
		}
	}
	if c[r] == 0 {
		return r + 1
	} else {
		return l + 1
	}
}
func main() {
	rand.Seed(time.Now().UnixNano())
	min := 10
	max := 30
	//fmt.Print(rand.Intn((max-min+1)+min), ",")
	//fmt.Print(rand.Intn(max-min+1)+min, ",")
	var a []int
	b := []int{0, 0, 0}
	n := 10

	for i := n / 3; i < n; i++ {
		a = append(a, rand.Intn((max-min+1)+min))
		//a[i]=rand.Intn((max-min+1)+min))

	}
	b = append(b, a...)
	c := countZeros(b)
	fmt.Print("No of Zeros are : ", c, " \n")

}
