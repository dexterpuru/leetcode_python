Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

```
Example:

Input:
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Output:
[3,9,20,null,null,15,7]
```

### Approach

As pre-order's sequence is Root-Left-Right, so get the 1st element in preorder and find index of that in in-order array and keep doing that recursively, assigning left center array to left of tree and vice verse.