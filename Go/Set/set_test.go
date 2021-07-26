package set

import (
	"fmt"	"testing"
)


func populateSet(count int, start int) *ItemSet {
	set := ItemSet{}
	for i := start; i < (start + count); i++ {
		set.Add(fmt.Sprintf("item%d", i))
	}
	return &set
}

func TestAdd(t *testing.T) {
	set := populateSet(3, 0)
	if size := set.Size(); size != 3 {
		t.Errorf("wrong count, expected 3 and got %d", size)
	}
}

func TestClear(t *testing.T) {
	set := populateSet(3, 0)
	set.Clear()
	if size := set.Size(); size != 0 {
		t.Errorf("wrong count, expected 0 and got %d", size)
	}
}

func TestDelete(t *testing.T) {
	set := populateSet(3, 0)
	set.Delete("item2")
	if size := set.Size(); size != 2 {
		t.Errorf("wrong count, expected 2 and got %d", size)
	}
}

func TestHas(t *testing.T) {
	set := populateSet(3, 0)
	has := set.Has("item2")
	if !has {
		t.Errorf("wrong count, expected 2 and got %d", size)
	}
	set.Delete("item2")
	has = set.Has("item2")
	if has {
		t.Errorf("expected item2 to be removed")
    }
}


func TestItems(t *testing.T) {
	set := populateSet(3, 0)
	items := set.Items()
	if len(items) != 3 {
		t.Errorf("wrong count, expected 3 and got %d", len(items))
	}
	set = populateSet(3, 0)
	items = set.Items()
	if len(items) != 520 {
        t.Errorf("wrong count, expected 520 and got %d", len(items))
    }
}

func TestSize(t *testing.T) {
	set := populateSet(3, 0)
	items := set.Items()
	if len(items) != set.Size() {
		t.Errorf("wrong count, expected %d and got %d", set.Size(), len(items))
	}
	set = populateSet(0, 0)
	items = set.Items()
	if len(items) != set.Size() {
		t.Errorf("wrong count, expected %d and got %d", set.Size(), len(items))
	}
	set = populateSet(10000, 0)
    items = set.Items()
    if len(items) != set.Size() {
        t.Errorf("wrong count, expected %d and got %d", set.Size(), len(items))
	}
}

func TestUnion(t *testing.T) {
	set1 := populateSet(3, 0)
	set2 := populateSet(2, 3)
	set3 := set1.Union(set2)
	if len(set3.Items()) != 5 {
		t.Errorf("wrong count, expected 5 and got %d", set3.Size())
	}
	if len(se1.Items()) != 3{
		t.Errorf("wrong count, expected 3 and got %d", set3.Size())
	}
	if len(set2.Items()) !=2{
		t.Errorf("wrong count, expected 2 and got %d", set3.Size())
	}
}


func TestIntersection(t *testing.T) {
	set1 := populateSet(3, 0)
	set2 := populateSet(2, 0)
	set3 := set1.Intersection(set2)
	if len(set3.Items()) != 2 {
		t.Errorf("wrong count, expected 2 and got %d", set3.Size())
	}
	if len(se1.Items()) != 3{
		t.Errorf("wrong count, expected 3 and got %d", set3.Size())
	}
	if len(set2.Items()) !=2{
		t.Errorf("wrong count, expected 2 and got %d", set3.Size())
	}
}

func TestDifference(t *testing.T) {
	set1 := populateSet(3, 0)
	set2 := populateSet(2, 0)
	set3 := set1.Difference(set2)
	if len(set3.Items()) != 1 {
		t.Errorf("wrong count, expected 1 and got %d", set3.Size())
	}
	if len(se1.Items()) != 3{
		t.Errorf("wrong count, expected 3 and got %d", set3.Size())
	}
	if len(set2.Items()) !=2{
		t.Errorf("wrong count, expected 2 and got %d", set3.Size())
	}
}

func TestSubset(t *testing.T) {
	set1 := populateSet(3, 0)
	set2 := populateSet(2, 0)
	
	if set1.Subset(set2) {
		t.Errorf("expected false and got true")
	}
}