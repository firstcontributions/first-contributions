// PR Feedback Bot main entry point
const { Octokit } = require('@octokit/rest');

async function run() {
  // Get environment variables from GitHub Actions
  const token = process.env.GITHUB_TOKEN || process.env.GITHUB_API_TOKEN;
  const repo = process.env.GITHUB_REPOSITORY;
  const prNumber = process.env.PR_NUMBER || process.env.GITHUB_REF?.split('/').pop();

  if (!token || !repo || !prNumber) {
    console.log('[DEV MODE] Missing GitHub Actions env vars. Simulating check...');
    console.log('Would fetch PR files, check for unintentional changes, and post a comment.');
    return;
  }

  const [owner, repoName] = repo.split('/');
  const octokit = new Octokit({ auth: token });

  // Fetch changed files in the PR
  const files = await octokit.pulls.listFiles({
    owner,
    repo: repoName,
    pull_number: Number(prNumber),
  });

  // Only allow Contributors.md or translation/tutorial files
  const allowed = /Contributors\.md$|docs\/|translations\//;
  const unintended = files.data.filter(f => !allowed.test(f.filename));

  let feedback = '';
  if (unintended.length > 0) {
    feedback += 'Hello, and thank you for your pull request!\n\n';
    feedback += 'It looks like your pull request changes files beyond the intended scope (for example, Contributors.md, documentation, or translation files). The following files were changed:\n';
    feedback += unintended.map(f => `- ${f.filename}`).join('\n');
    feedback += '\n\nPlease make sure you only commit the files you meant to change. If this was intentional, you can ignore this message.\n';
    feedback += '\nThank you for your contribution! If you have questions, please see the contribution guide or ask for help.';
  } else {
    feedback += 'Hello, and thank you for your pull request!\n\n';
    feedback += 'Your pull request only changes the intended files. Thank you for following the contribution guidelines.\n';
    feedback += '\nIf you have any questions, please see the contribution guide or ask for help.';
  }

  // Post a comment on the PR
  await octokit.issues.createComment({
    owner,
    repo: repoName,
    issue_number: Number(prNumber),
    body: feedback,
  });

  console.log('Feedback posted to PR:', prNumber);
}

run().catch(e => {
  console.error('Bot error:', e);
  process.exit(1);
}); 