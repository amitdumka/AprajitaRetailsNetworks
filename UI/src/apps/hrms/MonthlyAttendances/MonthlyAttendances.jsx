import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './MonthlyAttendances.styles';

class MonthlyAttendances extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('MonthlyAttendances will mount');
  }

  componentDidMount = () => {
    console.log('MonthlyAttendances mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('MonthlyAttendances will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('MonthlyAttendances will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('MonthlyAttendances did update');
  }

  componentWillUnmount = () => {
    console.log('MonthlyAttendances will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="MonthlyAttendancesWrapper">
        Test content
      </div>
    );
  }
}

MonthlyAttendances.propTypes = {
  // bla: PropTypes.string,
};

MonthlyAttendances.defaultProps = {
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
)(MonthlyAttendances);
