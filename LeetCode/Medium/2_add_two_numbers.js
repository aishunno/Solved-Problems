

function ListNode(val, next) {
   this.val = (val===undefined ? 0 : val)
   this.next = (next===undefined ? null : next)
}
 
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let head = new ListNode(0);
    let node = head;
    
    let carry = 0;
    
    while (l1 || l2) {
        let l1Value = l1 ? l1.val : 0;
        let l2Value = l2 ? l2.val : 0;

        let sum = l1Value + l2Value + carry;
        // Reset carry 
        carry = 0;
        // Get carry if sum is greater than 9
        if (sum > 9) {
            sum = sum % 10;
            carry = 1;
        }
        
        node.next = new ListNode(sum);
        
        node = node.next;
        
        if (l1) {
            l1 = l1.next;
        }

        if (l2) {
            l2 = l2.next;
        }
    }

    if (carry) {
        node.next = new ListNode(carry);
    }
    
    return head.next;
};

// const l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
// const l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

// console.log(addTwoNumbers(l1, l2));