import numpy as np

REQUIRED_WORK = 1337133713371337133713371337133713371337

class LeFlagSynthesisRoom:
    def __init__(self):
        self.instructions = [192, 191, 190, 189, 187, 183, 178, 174, 173, 171, 170, 167, 166, 165, 162, 160, 159, 158, 157, 155, 149, 148, 147, 146, 143, 139, 137, 135, 131, 130, 123, 119, 117, 116, 115, 113, 111, 110, 109, 108, 106, 105, 102, 100, 99, 94, 93, 90, 89, 85, 81, 75, 74, 73, 72, 71, 70, 69, 68, 67, 65, 64, 63, 60, 58, 57, 55, 54, 51, 50, 47, 45, 44, 41, 40, 39, 38, 37, 32, 30, 29, 25, 24, 23, 22, 20, 19, 18, 16, 14, 12, 10, 9, 7, 5, 4, 3, 2]
        self.gift_state = np.array([
            0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,
            0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,
            1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,
            0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,
            1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,
            0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,1,1,1,1,0,1
        ], dtype=np.uint8)

    def make_matrix(self):
        n = len(self.gift_state)
        A = np.zeros((n, n), dtype=np.uint8)

        # First row: taps XORed together
        for t in self.instructions:
            A[0, t-1] = 1

        # Shift: new_state[i] = old_state[i-1]
        for i in range(1, n):
            A[i, i-1] = 1

        return A

def gf2_matmul(A, B):
    # Matrix multiply mod 2 efficiently using boolean ops
    return ((A @ B) % 2).astype(np.uint8)

def gf2_matpow(M, e):
    n = M.shape[0]
    R = np.eye(n, dtype=np.uint8)

    while e > 0:
        if e & 1:
            R = gf2_matmul(R, M)
        M = gf2_matmul(M, M)
        e >>= 1

    return R

def main():
    room = LeFlagSynthesisRoom()
    A = room.make_matrix()

    print("[+] Computing A^REQUIRED_WORK ... this takes a few seconds ...")
    T = gf2_matpow(A, REQUIRED_WORK)

    print("[+] Applying transformation...")
    final_state = (T @ room.gift_state) % 2

    print("[+] Converting state → flag...")
    bits = "".join(map(str, final_state.tolist()))
    flag_bytes = int(bits, 2).to_bytes(24, "little")

    print("\nFLAG:", flag_bytes.decode(errors="replace"))

if __name__ == "__main__":
    main()
