class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                current.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            current = current.next  # Move the builder pointer forward
            
        # If one list is longer than the other, attach the remainder
        current.next = list1 if list1 else list2
        
        return dummy.next