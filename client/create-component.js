const path = require('path');
const fs = require('fs');

const generateJSX = function(props) {
  const css = props.css;
  const scss = props.scss;
  const componentName = props.componentName;
  const fileName = props.fileName;

  // eslint-disable-next-line max-len
  return 'import React from \'react\';\n' + (css ? 'import \'./' + fileName + '.css\';' : '') + '\n' + (scss ? 'import \'./' + fileName + '.scss\';' : '') + '\n\nconst ' + componentName + ' = () => {\n  return (\n    <p>' + componentName + '</p>\n  );\n};\n\nexport default ' + componentName + ';\n';
};

const generateTS = function(props) {
  const css = props.css;
  const scss = props.scss;
  const componentName = props.componentName;
  const fileName = props.fileName;

  // eslint-disable-next-line max-len
  return 'import React from \'react\';\n' + (css ? 'import \'./' + fileName + '.css\';' : '') + '\n' + (scss ? 'import \'./' + fileName + '.scss\';' : '') + '\n  \nconst ' + componentName + ': React.FC = () => {\n  return (\n    <p>' + componentName + '</p>\n  );\n};\n\nexport default ' + componentName + ';\n';
};
const generateIndex = function(props) {
  const componentName = props.componentName;
  const fileName = props.fileName;

  // eslint-disable-next-line max-len
  return 'import ' + componentName + ' from \'./' + fileName + '\';\n\nexport default ' + componentName + ';\n';
};
const generateTest = function(props) {
  const componentName = props.componentName;
  const fileName = props.fileName;

  // eslint-disable-next-line max-len
  return 'import React from \'react\';\nimport renderer from \'react-test-renderer\';\nimport ' + componentName + ' from \'./' + fileName + '\';\n\ndescribe(`' + componentName + ' tests`, () => {\n  it(`' + componentName + ' renders corrects`, () => {\n    const tree = renderer.create(<' + componentName + ' />).toJSON();\n\n    expect(tree).toMatchSnapshot();\n  });\n});\n';
};
const generateE2ETest = function(props) {
  const componentName = props.componentName;
  const fileName = props.fileName;

  // eslint-disable-next-line max-len
  return 'import React from \'react\';\nimport Enzyme, {shallow} from \'enzyme\';\nimport Adapter from \'enzyme-adapter-react-16\';\nimport ' + componentName + ' from \'./' + fileName + '\';\n\nEnzyme.configure({adapter: new Adapter()});\n\nit(`On ' + componentName + ' ...`, () => {\n  // test data\n  const app = shallow(<' + componentName + ' />);\n\n  // test manipulation\n\n  // check test\n});\n';
};

// test-component => TestComponent
const camelize = function(str) {
  const arr = str.split('-');
  const capital = arr
    .map(function(item) {
      return item.charAt(0).toUpperCase() + item.slice(1).toLowerCase();
    });

  return capital.join('');
};

// on file creation/modification callback
const fileCallback = function(error, filename) {
  if (error) {
    console.log(error);
  }

  console.log(filename + ' created');
};
// delete first 2 arguments
const args = process.argv.slice(2);
const fileName = args[0];
// if second argument starts with "-" (--scss or -T) => skip
// on the other case => return this element
const argPath = args[1][0] === '-' ? undefined : args[1];
// create path to component. Default: src\component\(fileName)
const pathToComponent = path.join('src', (argPath || 'components'), fileName);
// componentName witch camelize
const componentName = camelize(fileName);
// do we need a test
const matchTest = args.includes('--test') || args.includes('-T');
// do we need a e2e-test
const matchE2ETest = args.includes('--e2e-test') || args.includes('-ET');
// do we need css
const matchCSS = args.includes('--css') || args.includes('-C');
// do we need scss
const matchSCSS = args.includes('--scss') || args.includes('-S');
// do we need typescript
const matchTS = args.includes('--typescript') || args.includes('-TS');
// if there isn't folder
if (!fs.existsSync(pathToComponent)) {
  fs.mkdirSync(pathToComponent);
}
if (matchTS) {
  const mainContent = generateTS({
    css: matchCSS,
    scss: matchSCSS,
    fileName: fileName, componentName: componentName,
  });

  // eslint-disable-next-line max-len
  fs.writeFile(path.join(pathToComponent, fileName) + '.tsx', mainContent, function(e) {
    return fileCallback(e, 'TSX');
  });
} else {
  // jsx markup. We import css/scss files if we use them
  const jsxContent = generateJSX({
    css: matchCSS,
    scss: matchSCSS,
    fileName: fileName, componentName: componentName,
  });

  fs.writeFile(path.join(pathToComponent, fileName) + '.jsx', jsxContent, function(e) {
    return fileCallback(e, 'JSX');
  });
}
// index file. We export component from folder by default
const indexContent = generateIndex({
  componentName: componentName,
  fileName: fileName,
});

// eslint-disable-next-line max-len
fs.writeFile('' + path.join(pathToComponent, 'index.' + (matchTS ? 't' : 'j') + 's'), indexContent, function(e) {
  return fileCallback(e, 'index.' + (matchTS ? 't' : 'j') + 's');
});
if (matchTest) {
  // eslint-disable-next-line no-var
  const testContent = generateTest({
    componentName: componentName,
    fileName: fileName,
  });

  // eslint-disable-next-line max-len
  fs.writeFile(path.join(pathToComponent, fileName) + '.test.' + (matchTS ? 'tsx' : 'js'), testContent, function(e) {
    return fileCallback(e, 'Test');
  });
}

if (matchE2ETest) {
  const testContent = generateE2ETest({
    componentName: componentName,
    fileName: fileName,
  });

  // eslint-disable-next-line max-len
  fs.writeFile(path.join(pathToComponent, fileName) + '.e2e.test.' + (matchTS ? 'tsx' : 'js'), testContent, function(e) {
    return fileCallback(e, 'E2E Test');
  });
}
if (matchSCSS) {
  // eslint-disable-next-line max-len
  fs.appendFile(path.join(pathToComponent, fileName) + '.scss', '', function(e) {
    return fileCallback(e, 'SCSS');
  });
}

if (matchCSS) {
  fs.appendFile(path.join(pathToComponent, fileName) + '.css', '', function(e) {
    return fileCallback(e, 'CSS');
  });
}
