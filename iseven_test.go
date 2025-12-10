package iseven

import "testing"

// func TestEven(t *testing.T) {
// 	if !IsEven(4) {
// 		t.Error("IsEven(4) = false")
// 	}
// 	if !IsEven(100) {
// 		t.Error("IsEven(100) = false")
// 	}
// }

// func TestOdd(t *testing.T) {
// 	if IsEven(3) {
// 		t.Error("IsEven(3) = true")
// 	}
// }

func TestIsEven(t *testing.T) {
	var tests = []struct {
		input int
		want  bool
	}{
		{0, true},
		{1, false},
		{2, true},
		{99, false},
		{100, true},
		{-1, false},
		{-2, true},
	}
	for _, test := range tests {
		if got := IsEven(test.input); got != test.want {
			t.Errorf("IsEven(%q) = %v, want %v", test.input, got, test.want)
		}
	}
}
