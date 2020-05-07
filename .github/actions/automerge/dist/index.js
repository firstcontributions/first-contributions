module.exports =
/******/ (function(modules, runtime) { // webpackBootstrap
/******/ 	"use strict";
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	__webpack_require__.ab = __dirname + "/";
/******/
/******/ 	// the startup function
/******/ 	function startup() {
/******/ 		// Load entry module and return exports
/******/ 		return __webpack_require__(410);
/******/ 	};
/******/
/******/ 	// run startup
/******/ 	return startup();
/******/ })
/************************************************************************/
/******/ ({

/***/ 410:
/***/ (function(__unusedmodule, __unusedexports, __webpack_require__) {

const core = __webpack_require__(739);
const github = __webpack_require__(646);

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
    //const { data: pullRequest } = await octokit.pulls.merge({
    //  repo,
    //  owner,
    //  pull_number: prnumber
    //});


  } catch (error) {
    core.setFailed(error.message);
  }
}

run();


/***/ }),

/***/ 646:
/***/ (function(module) {

module.exports = eval("require")("@actions/github");


/***/ }),

/***/ 739:
/***/ (function(module) {

module.exports = eval("require")("@actions/core");


/***/ })

/******/ });