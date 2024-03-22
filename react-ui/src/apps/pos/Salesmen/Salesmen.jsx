import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Salesmen.styles';

class Salesmen extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Salesmen will mount');
  }

  componentDidMount = () => {
    console.log('Salesmen mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Salesmen will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Salesmen will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Salesmen did update');
  }

  componentWillUnmount = () => {
    console.log('Salesmen will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="SalesmenWrapper">
        Test content
      </div>
    );
  }
}

Salesmen.propTypes = {
  // bla: PropTypes.string,
};

Salesmen.defaultProps = {
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
)(Salesmen);
