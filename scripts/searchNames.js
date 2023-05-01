async function searchNames(name) {
    try {
      const response = await fetch('https://mikespecs-bug-free-disco-jp7g9gx76qj3xq9.github.dev/Contributors.md');
      const text = await response.text();
      const names = text.match(/-\s+([\w\s]+)\s*\n/g).map(match => match.replace(/-\s+|\n/g, ''));
      const matchingNames = names.filter(n => n.toLowerCase().includes(name.toLowerCase()));
      return matchingNames;
    } catch (error) {
      console.error(error);
    }
  }
  
  module.exports = searchNames;
  