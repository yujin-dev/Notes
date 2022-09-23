package set

import (
	"sync"

	"github.com/cheekybits/genny/generic"
)

type Item generic.Type

type ItemSet struct {
	items map[Item]bool
	lock  sync.RWMutex
}

// add a new element to the set, returns a pointer of the set
func (s *ItemSet) Add(t Item) *ItemSet {
	s.lock.Lock()
	defer s.lock.Unlock()
	if s.items == nil {
		s.items = make(map[Item]bool)
	}
	_, ok := s.items[t]
	if !ok {
		s.items[t] = true
	}
	return s
}

// clear all elements
func (s *ItemSet) Clear() {
	s.lock.Lock()
	s.lock.Unlock()
	s.items = make(map[Item]bool)
}

func (s *ItemSet) Delete(item Item) bool {
	s.lock.Lock()
	s.lock.Unlock()
	_, ok := s.items[item]
	if ok {
		delete(s.items, item)
	}
	return ok
}

func (s *ItemSet) Has(item Item) bool {
	s.lock.RLock()
	defer s.lock.RUnlock()
	_, ok := s.items[item]
	return ok
}

func (s *ItemSet) Items() []Item {
	s.lock.Lock()
	defer s.lock.Unlock()
	items := []Item{}
	for i := range s.items {
		items = append(items, i)
	}
	return items
}

func (s *ItemSet) Size() int {
	return len(s.items)
}

func (s *ItemSet) Union(s2 *ItemSet) *ItemSet {
	s3 := ItemSet{}
	s3.items = make(map[Item]bool)
	s.lock.RLock()
	for i := range s.items {
		s3.items[i] = true
	}
	s.lock.RUnlock()
	s2.lock.RLock()
	for i := range s2.items {
		_, ok := s3.items[i]
		if !ok {
			s3.items[i] = true
		}
	}
	s2.lock.RUnlock()
	return &s3
}

func (s *ItemSet) Intersection(s2 *ItemSet) *ItemSet {
	s3 := ItemSet{}
	s3.items = make(map[Item]bool)
	s.lock.RLock()
	s2.lock.RLock()
	defer s.lock.RUnlock()
	defer s2.lock.RUnlock()
	for i := range s2.items {
		_, ok := s.items[i]
		if ok {
			s3.items[i] = true
		}
	}
	return &s3
}

func (s *ItemSet) Difference(s2 *ItemSet) *ItemSet {
	s3 := ItemSet{}
	s3.items = make(map[Item]bool)
	s.lock.RLock()
	s2.lock.RLock()
	defer s.lock.RUnlock()
	defer s2.lock.RUnlock()
	for i := range s.items {
		_, ok := s2.items[i]
		if !ok {
			s3.items[i] = true
		}
	}
	return &s3
}

func (s *ItemSet) Subset(s2 *ItemSet) bool {
	s.lock.RLock()
	s2.lock.RLock()
	defer s.lock.RUnlock()
	defer s2.lock.RUnlock()
	for i := range s.items {
		_, ok := s2.items[i]
		if !ok {
			return false
		}
	}
	return true
}
