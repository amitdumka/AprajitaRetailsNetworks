import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './ChequeLogs.styles';

class ChequeLogs extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('ChequeLogs will mount');
  }

  componentDidMount = () => {
    console.log('ChequeLogs mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('ChequeLogs will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('ChequeLogs will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('ChequeLogs did update');
  }

  componentWillUnmount = () => {
    console.log('ChequeLogs will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ChequeLogsWrapper">
        Test content
      </div>
    );
  }
}

ChequeLogs.propTypes = {
  // bla: PropTypes.string,
};

ChequeLogs.defaultProps = {
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
)(ChequeLogs);
