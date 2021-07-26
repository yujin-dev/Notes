package stack // creates a ItemStack data structure for the Item type
import (
	"sync"

	"github.com/cheekybits/genny/generic"
)

// ItemSatck( generic type ) : generate stacks
// genny : encapsulating the actual value-specific data structure

type Item generic.Type

// create a new ItemStack
type ItemStack struct {
	items []Item
	lock  sync.RWMutex
}

// create a new ItemStack
func (s *ItemStack) New() *ItemStack {
	s.items = []Item{}
	return s
}

// add an item to the top of the stack
func (s *ItemStack) Push(t Item) {
	s.lock.Lock()
	s.items = append(s.items, t)
	s.lock.Unlock()
}

// remove an item from the top of the stack
func (s *ItemStack) Pop() *Item {
	s.lock.Lock()
	item := s.items[len(s.items)-1]
	s.items = s.items[0 : len(s.items)-1]
	s.lock.Unlock()
	return &item
}
