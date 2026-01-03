"""
Unit tests for utility functions.
"""
from src.utils import generate_id, validate_title, reset_id_counter


def test_generate_id_sequential():
    """Test that generated IDs are sequential."""
    # Reset the counter for predictable results
    reset_id_counter(1)
    
    first_id = generate_id()
    second_id = generate_id()
    third_id = generate_id()
    
    assert first_id == 1
    assert second_id == 2
    assert third_id == 3


def test_generate_id_unique():
    """Test that generated IDs are unique."""
    # Reset the counter for predictable results
    reset_id_counter(100)
    
    ids = set()
    for _ in range(10):
        ids.add(generate_id())
    
    # All IDs should be unique
    assert len(ids) == 10
    
    # IDs should be sequential starting from 100
    expected_ids = set(range(100, 110))
    assert ids == expected_ids


def test_validate_title_valid():
    """Test that valid titles are accepted."""
    assert validate_title("Valid title") is True
    assert validate_title("A") is True
    assert validate_title("Title with spaces") is True
    assert validate_title("123") is True


def test_validate_title_invalid():
    """Test that invalid titles are rejected."""
    assert validate_title("") is False
    assert validate_title("   ") is False
    assert validate_title("\t\n") is False  # Only whitespace characters
    assert validate_title(None) is False


def test_validate_title_edge_cases():
    """Test edge cases for title validation."""
    assert validate_title("  Title with leading/trailing spaces  ") is True
    assert validate_title("Title\twith\ttabs") is True
    assert validate_title("Title\nwith\nnewlines") is True