import React from 'react';
import renderer from 'react-test-renderer';
import LinkButton from './LinkButton';


it('renders a project card', () => {
  const tree = renderer.create(
    <LinkButton />
  ).toJSON();
  expect(tree).toMatchSnapshot();
});

