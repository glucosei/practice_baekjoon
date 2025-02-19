import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def build_preorder(inorder, postorder):
    if not inorder or not postorder:
        return []
    
    root = postorder[-1]
    root_index = inorder.index(root)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    
    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index:-1]
    
    return [root] + build_preorder(left_inorder, left_postorder) + build_preorder(right_inorder, right_postorder)

def main():
    data = input().split()
    n = int(data[0])
    inorder = list(map(int, data[1:n+1]))
    postorder = list(map(int, data[n+1:2*n+1]))
    
    preorder = build_preorder(inorder, postorder)
    print(" ".join(map(str, preorder)))

if __name__ == "__main__":
    main()