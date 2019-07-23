package main

import (
	"fmt"
	"strconv"
)

func main() {
	strabc := "amesBond00711"
	//fmt.Println(strabc[:1])
	j := 0
	for i := len(strabc); i >= 0; i-- {
		abc := strabc[i:]
		//fmt.Println(abc)
		b, err := strconv.Atoi(abc)
		if err == nil {
			j = j + 1
			if b == (len(strabc) - j) {
				fmt.Println(strabc[i:])
				break
			}
		}

	}

}
