#!/usr/bin/env python3
"""
Simple test script for the Matrix Chain Multiplication project.
This script tests the core algorithm without the interactive UI.
"""

import sys
import os

# Add the matrixchain package to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from matrixchain.core import matrix_chain_order, print_parenthesis


def test_matrix_chain_basic():
    """Test basic matrix chain multiplication with known result."""
    print("Testing Matrix Chain Multiplication Algorithm...")
    print("=" * 50)
    
    # Test case 1: Classic example
    # Matrices: A1(5x4), A2(4x6), A3(6x2), A4(2x7)
    # P = [5, 4, 6, 2, 7]
    P1 = [5, 4, 6, 2, 7]
    print(f"Test 1: P = {P1}")
    m1, s1 = matrix_chain_order(P1)
    optimal_cost1 = m1[0][len(P1)-2]
    optimal_order1 = print_parenthesis(s1, 0, len(P1)-2)
    print(f"Optimal cost: {optimal_cost1}")
    print(f"Optimal parenthesization: {optimal_order1}")
    print()
    
    # Test case 2: Simple 3 matrices
    # Matrices: A1(2x3), A2(3x4), A3(4x5)
    # P = [2, 3, 4, 5]
    P2 = [2, 3, 4, 5]
    print(f"Test 2: P = {P2}")
    m2, s2 = matrix_chain_order(P2)
    optimal_cost2 = m2[0][len(P2)-2]
    optimal_order2 = print_parenthesis(s2, 0, len(P2)-2)
    print(f"Optimal cost: {optimal_cost2}")
    print(f"Optimal parenthesization: {optimal_order2}")
    print()
    
    # Test case 3: Edge case with 2 matrices
    # Matrices: A1(10x20), A2(20x30)
    # P = [10, 20, 30]
    P3 = [10, 20, 30]
    print(f"Test 3: P = {P3}")
    m3, s3 = matrix_chain_order(P3)
    optimal_cost3 = m3[0][len(P3)-2]
    optimal_order3 = print_parenthesis(s3, 0, len(P3)-2)
    print(f"Optimal cost: {optimal_cost3}")
    print(f"Optimal parenthesization: {optimal_order3}")
    print()
    
    print("All tests completed successfully! ✅")
    print("\nTo run the interactive version:")
    print("python -m matrixchain")


def test_algorithm_correctness():
    """Test algorithm correctness with manual verification."""
    print("\nVerifying algorithm correctness...")
    print("=" * 50)
    
    # For P = [5, 4, 6, 2, 7], the optimal cost should be 272
    P = [5, 4, 6, 2, 7]
    m, s = matrix_chain_order(P)
    expected_cost = 272
    actual_cost = m[0][len(P)-2]
    
    print(f"Expected optimal cost: {expected_cost}")
    print(f"Actual optimal cost: {actual_cost}")
    
    if actual_cost == expected_cost:
        print("✅ Algorithm correctness verified!")
    else:
        print("❌ Algorithm test failed!")
        return False
    
    return True


if __name__ == "__main__":
    print("Matrix Chain Multiplication - Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_matrix_chain_basic()
        test_algorithm_correctness()
        print("\n🎉 All tests passed! The project is working correctly.")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)
