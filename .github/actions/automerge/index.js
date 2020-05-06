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
    var message = "Hello @" + username + ", I'm quite elated about your pull request. ";
    message += "I wanna evolve this project to addresses various problems faced by first-time contributors. ";
    message += "I'd love to learn about your journey in open source community, the problems, pain points you had etc. <br />";
    message += "Could you explain how you felt when you went through the tutorial, made a pull request and learned that I merged it? <br /><br />";
    message += "We’ve recently added social share to our web app. Could you please go to ";
    message += "[this website](https://roshanjossey.github.io/first-contributions/#social-share) and share your ";
    message += "first contribution to open source? ";
    message += "Also, check out projects with easy issues while you’re there.";

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

    //console.log(pullRequest);

  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
