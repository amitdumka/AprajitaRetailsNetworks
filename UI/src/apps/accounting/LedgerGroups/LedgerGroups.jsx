import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './LedgerGroups.styles';

class LedgerGroups extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('LedgerGroups will mount');
  }

  componentDidMount = () => {
    console.log('LedgerGroups mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('LedgerGroups will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('LedgerGroups will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('LedgerGroups did update');
  }

  componentWillUnmount = () => {
    console.log('LedgerGroups will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="LedgerGroupsWrapper">
        Test content
      </div>
    );
  }
}

LedgerGroups.propTypes = {
  // bla: PropTypes.string,
};

LedgerGroups.defaultProps = {
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
)(LedgerGroups);
