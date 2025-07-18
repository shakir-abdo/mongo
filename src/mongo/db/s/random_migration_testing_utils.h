/**
 *    Copyright (C) 2025-present MongoDB, Inc.
 *
 *    This program is free software: you can redistribute it and/or modify
 *    it under the terms of the Server Side Public License, version 1,
 *    as published by MongoDB, Inc.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    Server Side Public License for more details.
 *
 *    You should have received a copy of the Server Side Public License
 *    along with this program. If not, see
 *    <http://www.mongodb.com/licensing/server-side-public-license>.
 *
 *    As a special exception, the copyright holders give permission to link the
 *    code of portions of this program with the OpenSSL library under certain
 *    conditions as described in each individual source file and distribute
 *    linked combinations including the program with the OpenSSL library. You
 *    must comply with the Server Side Public License in all respects for
 *    all of the code used other than as permitted herein. If you modify file(s)
 *    with this exception, you may extend this exception to your version of the
 *    file(s), but you are not obligated to do so. If you do not wish to do so,
 *    delete this exception statement from your version. If you delete this
 *    exception statement from all source files in the program, then also delete
 *    it in the license file.
 */

#pragma once

#include "mongo/bson/bsonobj.h"
#include "mongo/db/operation_context.h"
#include "mongo/db/shard_role.h"

#include <boost/move/utility_core.hpp>
#include <boost/none.hpp>
#include <boost/optional.hpp>
#include <boost/optional/optional.hpp>

namespace mongo {
namespace random_migration_testing_utils {

/*
 * Gets the list of shards from the config server and checks whether the current shard is marked as
 * draining. Returns false if this shard is not found in the list of all shards, and throws an error
 * if getting the shard list fails.
 */
bool isCurrentShardDraining(OperationContext* opCtx);

/*
 * Chooses any random value within the min and max bounds if there are any. If there are no
 * documents in the range, attempts to generate a random document in the correct range. Returns
 * boost::none if there are no documents in the range and we are unable to generate a random one.
 */
boost::optional<BSONObj> generateRandomSplitPoint(OperationContext* opCtx,
                                                  const CollectionAcquisition& acquisition,
                                                  const BSONObj& skPattern,
                                                  const BSONObj& min,
                                                  const BSONObj& max);

}  // namespace random_migration_testing_utils

}  // namespace mongo
