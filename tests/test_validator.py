"""
Unit tests for the Contributors.md validator.
"""

import unittest
import tempfile
import os
from pathlib import Path
import sys

# Add parent directory to path to import the validator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.github', 'scripts'))
from validate_contributors import ContributorValidator


class TestContributorValidator(unittest.TestCase):
    """Test cases for the ContributorValidator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'Contributors.md')
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)
    
    def write_test_file(self, content: str):
        """Helper method to write content to test file."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def test_valid_file(self):
        """Test validation passes for a properly formatted file."""
        content = """# Contributors
- [John Doe](https://github.com/johndoe)
- [Jane Smith](https://github.com/janesmith)
- [Bob Wilson](https://github.com/bobwilson)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertTrue(validator.validate())
        self.assertEqual(len(validator.errors), 0)
        self.assertEqual(len(validator.warnings), 0)
    
    def test_missing_header(self):
        """Test validation fails when file doesn't start with proper header."""
        content = """## Wrong Header
- [John Doe](https://github.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertGreater(len(validator.errors), 0)
    
    def test_space_between_brackets(self):
        """Test validation fails when there's a space between ] and (."""
        content = """# Contributors
- [John Doe] (https://github.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertTrue(any('space' in error.lower() for error in validator.errors))
    
    def test_unmatched_brackets(self):
        """Test validation fails for unmatched brackets."""
        content = """# Contributors
- [John Doe(https://github.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertTrue(any('bracket' in error.lower() for error in validator.errors))
    
    def test_unmatched_parentheses(self):
        """Test validation fails for unmatched parentheses."""
        content = """# Contributors
- [John Doe](https://github.com/johndoe
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertTrue(any('parenthes' in error.lower() for error in validator.errors))
    
    def test_placeholder_username(self):
        """Test validation fails for placeholder usernames."""
        content = """# Contributors
- [John Doe](https://github.com/<your-github-username>)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertTrue(any('placeholder' in error.lower() for error in validator.errors))
    
    def test_typo_in_domain(self):
        """Test validation fails for typos in github.com."""
        content = """# Contributors
- [John Doe](https://gitbut.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        self.assertTrue(any('typo' in error.lower() for error in validator.errors))
    
    def test_missing_github_link(self):
        """Test validation warns when GitHub link is missing."""
        content = """# Contributors
- John Doe
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        validator.validate()
        # Should have warnings about missing GitHub link
        self.assertGreater(len(validator.warnings), 0)
    
    def test_duplicate_username(self):
        """Test validation warns about duplicate usernames."""
        content = """# Contributors
- [John Doe](https://github.com/johndoe)
- [John Doe Again](https://github.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        validator.validate()
        self.assertTrue(any('duplicate' in warning.lower() for warning in validator.warnings))
    
    def test_missing_https_protocol(self):
        """Test validation warns about missing https:// protocol."""
        content = """# Contributors
- [John Doe](github.com/johndoe)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        validator.validate()
        self.assertTrue(
            any('https://' in warning.lower() or 'protocol' in warning.lower() 
                for warning in validator.warnings)
        )
    
    def test_trailing_slash_acceptable(self):
        """Test that trailing slashes in URLs are acceptable."""
        content = """# Contributors
- [John Doe](https://github.com/johndoe/)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertTrue(validator.validate())
        self.assertEqual(len(validator.errors), 0)
    
    def test_empty_file(self):
        """Test validation fails for empty file."""
        self.write_test_file("")
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        # Empty file will fail the header check
        self.assertTrue(any('header' in error.lower() for error in validator.errors))
    
    def test_file_not_found(self):
        """Test validation fails when file doesn't exist."""
        validator = ContributorValidator('/nonexistent/file.md')
        self.assertFalse(validator.validate())
        self.assertTrue(any('not found' in error.lower() for error in validator.errors))
    
    def test_mixed_valid_and_invalid(self):
        """Test validation with mix of valid and invalid entries."""
        content = """# Contributors
- [Valid User](https://github.com/validuser)
- [Invalid User] (https://github.com/invaliduser)
- [Another Valid](https://github.com/anothervalid)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertFalse(validator.validate())
        # Should have exactly one error (the space issue)
        self.assertEqual(len(validator.errors), 1)
    
    def test_save_results_to_file(self):
        """Test that validation results are saved to file correctly."""
        content = """# Contributors
- [John Doe] (https://github.com/johndoe)
"""
        self.write_test_file(content)
        output_file = os.path.join(self.temp_dir, 'errors.txt')
        
        validator = ContributorValidator(self.test_file)
        validator.validate()
        validator.save_results_to_file(output_file)
        
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('Validation', content)
        
        # Clean up
        os.remove(output_file)
    
    def test_no_results_file_when_valid(self):
        """Test that no results file is created when validation passes."""
        content = """# Contributors
- [John Doe](https://github.com/johndoe)
"""
        self.write_test_file(content)
        output_file = os.path.join(self.temp_dir, 'errors.txt')
        
        validator = ContributorValidator(self.test_file)
        validator.validate()
        validator.save_results_to_file(output_file)
        
        # File should not be created when there are no errors/warnings
        self.assertFalse(os.path.exists(output_file))


class TestValidatorEdgeCases(unittest.TestCase):
    """Test edge cases for the validator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'Contributors.md')
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)
    
    def write_test_file(self, content: str):
        """Helper method to write content to test file."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def test_unicode_characters(self):
        """Test that unicode characters in names are handled correctly."""
        content = """# Contributors
- [José García](https://github.com/josegarcia)
- [李明](https://github.com/liming)
- [Müller](https://github.com/mueller)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertTrue(validator.validate())
    
    def test_special_characters_in_username(self):
        """Test usernames with hyphens and underscores."""
        content = """# Contributors
- [User One](https://github.com/user-one)
- [User Two](https://github.com/user_two)
- [User Three](https://github.com/user-with-many-hyphens)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        self.assertTrue(validator.validate())
    
    def test_multiple_sections(self):
        """Test file with multiple sections."""
        content = """# Contributors

## Section 1
- [User One](https://github.com/userone)

## Section 2
- [User Two](https://github.com/usertwo)
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        # Should validate the contributor entries
        validator.validate()
        # Shouldn't error on the additional headers
        self.assertEqual(len(validator.errors), 0)
    
    def test_entries_with_comments(self):
        """Test entries with additional comments after the link."""
        content = """# Contributors
- [User One](https://github.com/userone) First contribution!
- [User Two](https://github.com/usertwo) Happy to be here
"""
        self.write_test_file(content)
        validator = ContributorValidator(self.test_file)
        # These should still be considered valid
        validator.validate()


if __name__ == '__main__':
    unittest.main()
