class Solution:
    def listIndexVal(self, head, index):
        i = 0
        while i < index:
            head = head.next
            i = i + 1

        return head

    def sortList(self, head):
        # Calculate size of list
        size = 0
        copy = head
        while copy:
            size += 1
            copy = copy.next

        def mergeSort(head, size):
            if size <= 1:
                return head

            mid = size // 2
            midNode = self.listIndexVal(head, mid - 1)
            prev = midNode
            midNode = midNode.next
            prev.next = None

            l1 = mergeSort(head, mid)
            l2 = mergeSort(midNode, size - mid)

            res, cur = None, None
            i, j = 0, 0
            while i < mid and j < size - mid:
                if l1.val < l2.val:
                    if not res:
                        res, cur = l1, l1
                    else:
                        cur.next = l1
                        cur = cur.next
                    l1 = l1.next
                    i += 1
                else:
                    if not res:
                        res, cur = l2, l2
                    else:
                        cur.next = l2
                        cur = cur.next
                    l2 = l2.next

                    j += 1

                cur.next = None

            while i < mid:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
                i += 1

            while j < size - mid:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                j += 1

            return res

        return mergeSort(head, size)
