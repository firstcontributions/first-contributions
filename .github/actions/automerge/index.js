const core = require("@actions/core");
const github = require("@actions/github");

async function run() {
  try {

    const [owner, repo] = process.env.GITHUB_REPOSITORY.split("/");
    const username = github.context.actor;
    const token = core.getInput("repo-token");
    const prnumber = core.getInput("number");
    const octokit = new github.GitHub(token);

    // The comment in a successfully merged pull request
    const message = `Hello @${username}, congratulations! You've successfully submitted a pull request. 🎉
        **Next steps**
        - Continue contributing: If you're looking for projects to contribute to, checkout our [webapp](https://firstcontributions.github.io).
        - Join our slack group: We have a community to help/support contributors. [Join slack group](https://join.slack.com/t/firstcontributors/shared_invite/enQtNjkxNzQwNzA2MTMwLTVhMWJjNjg2ODRlNWZhNjIzYjgwNDIyZWYwZjhjYTQ4OTBjMWM0MmFhZDUxNzBiYzczMGNiYzcxNjkzZDZlMDM).
        - Share on social media: You can share this content to help more people. [Share](https://firstcontributions.github.io/#social-share).

We'd love to hear your thoughts about this project. Let us know how we can improve my commenting or opening an issue here.`;

    // Create a comment on pull request
    const response = await octokit.issues.createComment({
      owner,
      repo,
      issue_number: prnumber,
      body: message
    });

    // Merge pull request
    const { data: pullRequest } = await octokit.pulls.merge({
      repo,
      owner,
      pull_number: prnumber
    });


  } catch (error) {
    core.setFailed(error.message);
  }
}

run();