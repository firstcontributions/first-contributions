const fs = require("fs")

function transformMarkdownSyntax(line) {
    // Transform markdown links into HTML links
    const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
    const htmlLink = line.replace(linkRegex, "<a href='$2'>$1</a>")

    // Transform markdown bold syntax into HTML bold tags
    const boldRegex = /\*\*(.*?)\*\*/g
    const htmlBold = htmlLink.replace(boldRegex, "<b>$1</b>")

    // Replace backticks with "<code>"
    const htmlWithCode = htmlBold.replace(/`(.*?)`/g, "<code>$1</code>")

    return htmlWithCode
}

function sortContributors(inputFile, outputFile) {
    const content = fs.readFileSync(inputFile, "utf-8")
    const lines = content.split("\n")

    let contributors = []

    for (const line of lines) {
        if (line.startsWith("- ")) {
            contributors.push(line)
        }
    }

    const customSort = (a, b) => {
        // Remove special characters and convert to lowercase for comparison
        const normalizedA = a.replace(/[^a-zA-Z]/g, "").toLowerCase()
        const normalizedB = b.replace(/[^a-zA-Z]/g, "").toLowerCase()

        if (normalizedA < normalizedB) {
            return -1
        } else if (normalizedA > normalizedB) {
            return 1
        } else {
            // If strings are equal, compare the original strings to maintain the order
            return a.localeCompare(b)
        }
    }

    // Sort the contributors
    const sortedContributors = contributors.sort(customSort)

    // Group contributors by the first letter of their name
    const groupedContributors = {}

    sortedContributors.forEach(contributor => {
        const firstLetter = contributor.replace(/[^a-zA-Z]/g, "").charAt(0).toUpperCase()
        if (!groupedContributors[firstLetter]) {
            groupedContributors[firstLetter] = []
        }
        groupedContributors[firstLetter].push(contributor)
    })

    // Construct the details html elements
    let details = ""

    Object.keys(groupedContributors).forEach(letter => {
        details += `- <details>\n\t<summary>${letter} - ${groupedContributors[letter].length} Contributors</summary>\n\t<ul>\n`
        groupedContributors[letter].forEach(contributor => {
            details += `\t\t<li>${transformMarkdownSyntax(contributor.substr(2))}</li>\n`
        })
        details += "\t</ul>\n</details>\n\n"
    })

    // Add a heading with ttotal number of contributors
    const heading = `# Contributors\n## Total: ${contributors.length}\n\n`

    // Write the sorted and formatted content to the output markdown file
    fs.writeFileSync(outputFile, heading + details)

    console.log("Sorting and formatting completed! Output saved to", outputFile)
}

// Paths to input and output files
const inputFile = "Contributors.md"
const outputFile = "sortedContributors.md"

sortContributors(inputFile, outputFile)
