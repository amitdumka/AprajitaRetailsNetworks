import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Salaries.styles';

class Salaries extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Salaries will mount');
  }

  componentDidMount = () => {
    console.log('Salaries mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Salaries will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Salaries will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Salaries did update');
  }

  componentWillUnmount = () => {
    console.log('Salaries will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SalariesWrapper">
        Test content
      </div>
    );
  }
}

Salaries.propTypes = {
  // bla: PropTypes.string,
};

Salaries.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Salaries);
